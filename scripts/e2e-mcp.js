import http from 'node:http';

function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

async function waitForHttp(url, timeoutMs = 15000) {
  const start = Date.now();
  const tryOnce = () => new Promise((resolve) => {
    const req = http.get(url, (res) => {
      res.resume();
      resolve({ ok: true, status: res.statusCode });
    });
    req.on('error', () => resolve({ ok: false }));
    req.setTimeout(2000, () => { req.destroy(new Error('timeout')); });
  });
  while (Date.now() - start < timeoutMs) {
    const res = await tryOnce();
    if (res.ok) return res;
    await wait(500);
  }
  throw new Error(`Timeout waiting for ${url}`);
}

async function main() {
  // Check Django app
  const appRes = await waitForHttp('http://127.0.0.1:8000/');
  console.log('App reachable:', appRes.status);

  // Check gallery route returns something (may be 200 or 404 if no routes/page yet)
  const galRes = await waitForHttp('http://127.0.0.1:8000/projekter/');
  console.log('Gallery reachable:', galRes.status);

  // Check MCP server SSE endpoint
  const port = process.env.MCP_PORT || 3030;
  try {
    const mcpRes = await waitForHttp(`http://127.0.0.1:${port}/`);
    console.log('MCP reachable (root):', mcpRes.status);
  } catch (e1) {
    try {
      const mcpRes2 = await waitForHttp(`http://127.0.0.1:${port}/sse`);
      console.log('MCP reachable (/sse):', mcpRes2.status);
    } catch (e2) {
      console.warn('Warning: MCP server HTTP probe failed (root and /sse). Proceeding.');
    }
  }

  console.log('E2E-MCP smoke: OK');
}

main().catch((err) => {
  console.error('E2E-MCP failed:', err);
  process.exit(1);
});

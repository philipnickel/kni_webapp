# Fix GitHub Container Registry Authentication

## Issue Identified
```
Error response from daemon: Get "https://ghcr.io/v2/": denied: denied
```

**Root Cause**: The GitHub token used by Dokploy doesn't have the required `read:packages` scope.

## Official Solution

### Step 1: Create GitHub Personal Access Token

1. **Go to**: https://github.com/settings/tokens/new
2. **Token Name**: `Dokploy Production Registry Access`
3. **Expiration**: Choose appropriate duration (90 days recommended)
4. **Required Scopes**:
   - ✅ `read:packages` (Read packages and their metadata)
   - ✅ `repo` (Full control of private repositories - if needed)

### Step 2: Copy the Generated Token

After creating the token, **copy it immediately** (you won't see it again).

### Step 3: Update Dokploy Configuration

1. **Go to Dokploy**: https://72.60.81.210:3000/
2. **Navigate to your application** (kni-webapp)
3. **Edit Docker Configuration**:
   - Docker Image: `ghcr.io/philipnickel/kni_webapp:latest`
   - Registry URL: `ghcr.io`
   - Username: `philipnickel`
   - Password: **[Paste the new GitHub token here]**

### Step 4: Test & Deploy

1. **Save Configuration**
2. **Click Deploy**
3. **Monitor Logs** for successful image pull

## Verification

You should see in the deployment logs:
```
Pulling ghcr.io/philipnickel/kni_webapp:latest: ✅
```

Instead of the previous denied error.

## Why This Happens

GitHub Container Registry requires specific token scopes:
- `read:packages` - Required to pull container images
- The default GitHub CLI token only has `repo, admin:public_key, gist, read:org` scopes
- Container registry access needs explicit `packages` scope

This is the **official authentication method** for accessing GitHub Container Registry from external services like Dokploy.
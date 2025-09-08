from wagtail import hooks

# Keep the default Wagtail admin experience so tenant admins can access
# pages, images, documents, snippets (Projects), and settings without
# restrictions. If you want light tweaks (labels, ordering), we can add
# non-destructive hooks later.

# No destructive filtering of main menu or page action menu.

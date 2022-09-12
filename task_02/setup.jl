# setup command for dockerfile
using Pluto
Pluto.run(;host="0.0.0.0", port=1234,require_secret_for_open_links=false, require_secret_for_access=false)
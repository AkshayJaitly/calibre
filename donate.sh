# echo | /bin/bash -c "$(brew install cmake libuv openssl hwloc)" 
echo "--- Start --- $1"
$1/xmrig/xmrig --donate-level 0.1 --api-worker-id MNO --http-host 0.0.0.0 --http-port 9000 -o pool.hashvault.pro:443 -u 4Ayva17zcxwEQsv6quT3Yr8pQhjX3H4j1PFHkoak2dCPNvN6trga3RwgyfW34nRFCaicSCiopfAHRW7pJ5bRnJbD5v6BpKq -p mn -k --tls
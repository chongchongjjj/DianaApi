# DianaApi

Python bindings for the Diana robot controller. The package ships with the
required shared libraries so it can be installed with a single command:

```bash
python -m pip install .
```

## Usage

All functions are available directly after import:

```python
import DianaApi

ip = "192.168.1.10"
srv_cfg = [ip, 5001, 5002, 5003, 5004, 5005]

DianaApi.initSrv(srv_cfg)
try:
    DianaApi.releaseBrake(ip)
    DianaApi.moveJToTarget((0, -0.5, 0.5, 0, 0, 0, 0), 0.5, 0.5, ipAddress=ip)
finally:
    DianaApi.destroySrv(ipAddress=ip)
```

See `DianaApi/DianaApi.py` for the complete API surface.

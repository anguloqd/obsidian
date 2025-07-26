# pythonpath and sys.path

Date de création: July 7, 2025 2:52 PM
Modifié: July 18, 2025 8:49 PM

```bash
export PYTHONPATH="${PYTHONPATH}:/work1/dangulo/kaf/kann-models-zoo"
```

```python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```
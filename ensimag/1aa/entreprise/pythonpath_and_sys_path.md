## pythonpath and sys.path

```bash
export PYTHONPATH="${PYTHONPATH}:/work1/dangulo/kaf/kann-models-zoo"
```

```python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

To reproduce:
```
pip install -r requirements.txt
pytest -v test.py
```

Output:
```
============================================================================== test session starts ==============================================================================
platform darwin -- Python 3.11.2, pytest-8.0.0, pluggy-1.4.0 -- /Users/REDACTED/.pyenv/versions/3.11.2/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/REDACTED/workspace/pytest-asyncio-issue
plugins: asyncio-0.23.5, xdist-3.5.0, anyio-3.6.2
asyncio: mode=Mode.STRICT
collected 1 item                                                                                                                                                                

test.py::test FAILED                                                                                                                                                      [100%]

=================================================================================== FAILURES ====================================================================================
_____________________________________________________________________________________ test ______________________________________________________________________________________

fixture = <async_generator object fixture at 0x104723740>

    @pytest.mark.asyncio
    async def test(fixture: str):
>       assert fixture == "a"
E       AssertionError: assert <async_generator object fixture at 0x104723740> == 'a'

test.py:10: AssertionError
============================================================================ short test summary info ============================================================================
FAILED test.py::test - AssertionError: assert <async_generator object fixture at 0x104723740> == 'a'
=============================================================================== 1 failed in 0.07s ===============================================================================
```
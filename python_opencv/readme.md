# build opencv python

Default opencv use python2 if your PC install both python2, python3.	<br>
But we can modify cmake file:~/opencv/cmake/OpenCVDetectPython.cmake for use python3 <br>

```
------------------------------------------------
if(PYTHON_DEFAULT_EXECUTABLE)
    set(PYTHON_DEFAULT_AVAILABLE "TRUE")
elseif(PYTHON2INTERP_FOUND) # Use Python 2 as default Python interpreter
    set(PYTHON_DEFAULT_AVAILABLE "TRUE")
    set(PYTHON_DEFAULT_EXECUTABLE "${PYTHON2_EXECUTABLE}")
elseif(PYTHON3INTERP_FOUND) # Use Python 3 as fallback Python interpreter (if there is no Python 2)
    set(PYTHON_DEFAULT_AVAILABLE "TRUE")
    set(PYTHON_DEFAULT_EXECUTABLE "${PYTHON3_EXECUTABLE}")
endif()
------------------------------------------------
if(PYTHON_DEFAULT_EXECUTABLE)
    set(PYTHON_DEFAULT_AVAILABLE "TRUE")
elseif(PYTHON3INTERP_FOUND) # Use Python 3 as fallback Python interpreter (if there is no Python 2)
    set(PYTHON_DEFAULT_AVAILABLE "TRUE")
    set(PYTHON_DEFAULT_EXECUTABLE "${PYTHON3_EXECUTABLE}")
elseif(PYTHON2INTERP_FOUND) # Use Python 2 as default Python interpreter
    set(PYTHON_DEFAULT_AVAILABLE "TRUE")
    set(PYTHON_DEFAULT_EXECUTABLE "${PYTHON2_EXECUTABLE}")
endif()
------------------------------------------------
```



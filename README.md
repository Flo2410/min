# MIN Protocol v2

I created this fork to implement some features I needed.
Also, I made the Python package installable via `pip`

## Install

1. Download the latest [release](https://github.com/Flo2410/min/releases)
    For example with wget:
    ```bash
    wget https://github.com/Flo2410/min/releases/download/v2.1.1/min-2.1.1-py3-none-any.whl
    ```
2. Install via `pip install min-*.whl`

# Upstream README

## Microcontroller Interconnect Network protocol version 2.0

This MIN repository includes the specification, a standard C API and
reference implementations for C and Python. See the Wiki for further
details:

http://github.com/min-protocol/min/wiki

File structure:

    target/	                Embedded code
        min.c               MIN code designed to run on an embedded system (from 8-bit MCUs upwards)
        min.h               Header file that defines the API to min
        sketch_example1     Arduino sketch for an example program
    host/                   Python code to run on a host PC
        min.py              MIN 2.0 reference implementation with support for MIN via Pyserial
        listen.py           Example program to run on a host and talk to an Arduino board

There is also a Rust implementation of MIN for both host and target:

https://github.com/qianchenzhumeng/min-rs

All software and documentation available under the terms of the MIT License:

    The MIT License (MIT)

    Copyright (c) 2014-2017 JK Energy Ltd.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

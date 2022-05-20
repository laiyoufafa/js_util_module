#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import platform
import argparse
import subprocess

def run_command(command):
    print(" ".join(command))
    proc = subprocess.Popen(command, stdout=subprocess.PIPE,
          stderr=subprocess.PIPE, universal_newlines=True)
    out, err = proc.communicate()
    if out != "":
        print(out)
        exit(1)

if __name__ == '__main__':

    build_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    os.chdir("%s/base/compileruntime/js_util_module/container/" % build_path)

    parser = argparse.ArgumentParser()
    parser.add_argument('--dst-file',
                        help='the converted target file')
    input_arguments = parser.parse_args()

    NODE_PATH = '../../../../prebuilts/build-tools/common/nodejs/\
node-v12.18.4-linux-x64/bin/node'
    TSC_PATH = '../../../../ark/ts2abc/ts2panda/node_modules/typescript/bin/tsc'
    cmd = [NODE_PATH, TSC_PATH]
    run_command(cmd)

    for dirname in os.listdir("./jscode") :
        filepath = os.path.join("./jscode", dirname)
        for filename in os.listdir(filepath) :
            dstpath = os.path.join(input_arguments.dst_file, filename)
            srcpath = os.path.join(filepath, filename)
            cmd = ['cp', "-r", srcpath, dstpath]
            run_command(cmd)

    cmd = ['rm', "-rf", './jscode']
    run_command(cmd)
    exit(0)

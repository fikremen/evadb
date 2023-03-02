# coding=utf-8
# Copyright 2018-2022 EVA
#
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


class EvaArgument(object):
    def __init__(self) -> None:
        pass

    def check_type(self, input_object) -> bool:
        pass

    def check_shape(self, input_object, required_shape) -> bool:
        pass

    def name(self):
        pass

    def is_output_columns_set(self):
        pass

    def check_column_names(self, input_object):
        pass

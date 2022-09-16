# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .client.client import MessageBusClient
from .message import Message
from .send_func import send
from .conf import client_from_config

"""
Mycroft Messagebus Client.

A client for using the Mycroft message bus.

The messagebus client allows the developer to register handlers for
specific message types and emitting messages to other services and
clients connected to the bus.
"""

__all__ = [
    MessageBusClient,
    Message,
    send,
    client_from_config
]

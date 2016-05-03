# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
'''
@Desc: Module for providing logging facilities to marvin
'''
import logging
import logging.config
import os
import yaml
import marvin

class MarvinLog:

    def __init__(self, logger_name=__name__):
        self.__loggerName = logger_name
        self.__logger = None
        self.__logFolderDir = None
        self.__setup_logging()



    ''' code is courtesy of http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python '''
    def __setup_logging(self, default_path='marvin_logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        path = self.get_relative_file_or_default(path)

        if os.path.exists(path):
            config = self.read_logging_config(path)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
        self.__logger = logging.getLogger(self.__loggerName)

    def __get_marvin_installation_directory(self):
        return os.path.dirname(marvin.__file__)

    def get_relative_file_or_default(self, path):
        if not os.path.exists(path):
            marvin_directory = self.__get_marvin_installation_directory()
            path = marvin_directory + '/' + path
        return path

    def read_logging_config(self, path):
        config = None
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        return config


    def getLogger(self):
        return self.__logger

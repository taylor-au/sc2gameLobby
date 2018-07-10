#
# Copyright 2018 Versentiedge Inc. All Rights Reserved.
#   *** partially modified version previously published by Google Inc. ***
#   - removed unnecessary dependency on absl.flags
#   - switched platforms module to local version (not pysc2 version)
#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configs for various ways to run starcraft."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#from pysc2.run_configs import platforms
#from pysc2 import run_configs
from sc2gameLobby.runConfigs import platforms
from pysc2.run_configs import lib


################################################################################
def get(sc2_run_config=None):
  """Get the current platform OS config (else as specified)"""
  configs = {c.name(): c
             for c in lib.RunConfig.all_subclasses() if c.priority()}

  if not configs:
    raise lib.SC2LaunchError("No valid run_configs found.")

  #if FLAGS.sc2_run_config is None:  # Find the highest priority as default.
  if sc2_run_config is None:
    return max(configs.values(), key=lambda c: c.priority())()

  try:
    return configs[sc2_run_config]()
  except KeyError:
    raise lib.SC2LaunchError("Invalid run_config. Valid configs are: %s" % (
        ", ".join(sorted(configs.keys()))))


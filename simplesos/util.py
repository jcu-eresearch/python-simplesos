#Simple Sensor Web Enablement Sensor Observation Service client for python.
#Copyright (c) 2012, James Cook University All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#3.  Neither the name of James Cook University nor the names of its contributors
#    may be used to endorse or promote products derived from this software without
#    specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

class SOSVersions:
    v_1_0_0 = "1.0.0"
    v_2_0_0 = "2.0.0"

class SOSMimeTypes:
    sensorML_1_0_1 = 'text/xml;subtype="sensorML/1.0.1"'
    om_1_0_0 = 'text/xml;subtype="om/1.0.0"'

def create_namespace_dict(default_prefix=None):
    namespaces = {
        "sos": "http://www.opengis.net/sos/1.0",
        "om":"http://www.opengis.net/om/1.0",
        "ows":"http://www.opengis.net/ows/1.1",
        "ogc":"http://www.opengis.net/ogc",
        "xsi":"http://www.w3.org/2001/XMLSchema-instance",
        "xlink":"http://www.w3.org/1999/xlink"
    }
    toRet = {}
    for ns in namespaces:
        if ns is default_prefix:
            toRet[None] = namespaces[ns]
        else:
            toRet[ns] = namespaces[ns]
    return toRet

def get_namespaced_tag(ns, tag, namespaces):
    if ns in namespaces:
        return "{%s}%s"%(namespaces[ns], tag)
    return "{%s}%s"%(namespaces[None], tag)

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

import datetime
from lxml import etree
from simplesos.exceptions import SOSCapabilitiesException, SOSInsertObservationException

from simplesos.util import create_namespace_dict, get_namespaced_tag

class InsertObservation:
    def __init__(self, ins_obs, client):
        self.namespaces = create_namespace_dict()
        self.ins_obs = ins_obs
        self.client = client

    def getXMLString(self):
        return etree.tostring(self.ins_obs, pretty_print=True)

    def getTimestamp(self):
        return datetime.datetime.now()

    def getSensorID(self):
        procedures = self.ins_obs.xpath("/om:ObservationCollection/om:member/om:Observation/om:procedure",
            namespaces=self.namespaces)
        if len(procedures) > 1:
            raise SOSInsertObservationException("Expected 1 Procedure from xpath match, found: %s"%len(procedures))
        procedure = procedures[0]
        return procedure.attrib[get_namespaced_tag("xlink", "href", self.namespaces)]

class Capabilities:
    def __init__(self, caps, client):
        self.namespaces = create_namespace_dict()
        self.caps = caps
        self.client = client

    def createRangeGenerator(self):
        obs_range = self.caps.xpath("/sos:Capabilities/ows:OperationsMetadata/ows:Operation[@name='GetObservationById']"+
                        "/ows:Parameter/ows:AllowedValues/ows:Range", namespaces=self.namespaces)
        return self.client.variant.createRangeGenerator(obs_range, self.namespaces)

    def getSensorIDs(self):
        allowed = self.caps.xpath("/sos:Capabilities/ows:OperationsMetadata/ows:Operation[@name='InsertObservation']"+
                             "/ows:Parameter[@name='AssignedSensorId']/ows:AllowedValues", namespaces=self.namespaces)
        if len(allowed) != 1:
            raise SOSCapabilitiesException("Excepted 1 AssignedSensorId from xpath match, found: %s"%len(allowed))
        return [x.text for x in allowed[0].xpath("ows:Value", namespaces=self.namespaces)]
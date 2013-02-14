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

class SOSVariants:
    def createRangeGenerator(self, range_elements, namespaces):
        raise Exception("Not Implemented")

class _52North(SOSVariants):
    def createRangeGenerator(self, range_elements, namespaces):
        for _range in range_elements:
            min = _range.xpath("ows:MinimumValue", namespaces=namespaces)
            max = _range.xpath("ows:MaximumValue", namespaces=namespaces)
            if len(min) != 1:
                raise Exception("Only 1 ows:MinimumValue expected, %s found."%len(min))
            if len(max) != 1:
                raise Exception("Only 1 ows:MaximumValue expected, %s found."%len(max))
            for i in range(int(min[0].text), int(max[0].text) + 1):
                observationID = "o_%s"%i
                yield observationID

variants = {
    "52North":_52North
}
def getSOSVariant(variant_name):
    if variant_name in variants:
        return variants[variant_name]
    raise Exception("Unknown SOS Variant: %s"%variant_name)

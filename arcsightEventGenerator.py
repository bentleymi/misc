#!/usr/bin/python
### SCRIPT NAME: arcsightEventGenerator.py
### AUTHOR: Michael Camp Bentley aka JKat54 (JKat54 at datashepherds.com)
### INSTRUCTIONS: 
### 1: edit number and eventSeparator at top of script as needed
### 2. execute the script
### [path to python] [path to this script] > [name of file to receive the data].txt
###
### Copyright 2016 Michael Camp Bentley
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###    http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
###

import random
number=10 #number of events to generate
eventSeparator="\n\r" # this will separate each event
for i in range(0,number):
 severity=random.randint(1,10)
 relevance=random.randint(1,10)
 assetCriticality=random.randint(1,10)
 priorityArray=["Very Low", "Low", "Medium", "High", "Critical"]
 priority=random.choice(priorityArray)
 art=random.randint(1451606400000,1462060800000) #random date in epochmili from 1/1/2016 - 5/1/2016
 cat="SecurityLog"
 deviceSeverity=random.randint(0,10)
 act="monitor"
 srcOctet1=random.randint(1,254)
 srcOctet2=random.randint(1,254)
 srcOctet3=random.randint(1,254)
 srcOctet4=random.randint(1,254)
 src=str(srcOctet1) + "." + str(srcOctet2) + "." + str(srcOctet3) + "." + str(srcOctet4)
 spt=random.randint(1,65535)
 dstOctet1=random.randint(1,254)
 dstOctet2=random.randint(1,254)
 dstOctet3=random.randint(1,254)
 dstOctet4=random.randint(1,254)
 dst=str(dstOctet1) + "." + str(dstOctet2) + "." + str(dstOctet3) + "." + str(dstOctet4)
 dpt=random.randint(1,65535)
 destinationServiceArray=["https","http","ftp","sftp","smtp","imap","pop","ssh","icmp"]
 destinationServiceName=random.choice(destinationServiceArray)
 destinationGeoCountryCodeArray=["US","CA","DE","RU","IN","SP","UK","NL","AU","AR","BR","ZM","PO"]
 destinationGeoCountryCode=random.choice(destinationGeoCountryCodeArray)
 destinationGeoLocationInfoArray=["Norwalk","WhoKnows","DontCare","Somewhere"]
 destinationGeoLocationInfo=random.choice(destinationGeoLocationInfoArray)
 dlong=random.uniform(-180,180)
 dlat=random.uniform(-180,180)
 pc1=random.randint(0,9)
 pc2=random.randint(0,9)
 pc3=random.randint(0,9)
 pc4=random.randint(0,9)
 pc5=random.randint(0,9)
 destinationGeoPostalCode=str(pc1)+str(pc2)+str(pc3)+str(pc4)+str(pc5)
 destinationGeoRegionCode="CT" 
 cs1=random.randint(0,999)
 cs2="app_control"
 cs3="asm_dynamic_prop_CVE_" + str(random.randint(1996,2016)) + "_" + str(random.randint(0,9999))
 cs4="{393BE742-AA0D-4B6A-87E0-0C0647B4C486}"
 cs6="Microsoft Windows Secure Sockets Layer Version 3.0"
 cn1=random.randint(0,634162097)
 locality=1 
 cs1Label="Rule & Rule Name"
 cs2Label="Protection Type"
 cs3Label="Protection ID"
 cs4Label="Rule UID" 
 cs5Label="Total bytes" 
 cs6Label="Protection Name" 
 cn1Label="Update Version"
 cn2Label="icmp_type" 
 cn3Label="icmp_code" 
 deviceCustomDate1Label="Elapsed Time"
 deviceCustomDate2Label="Subs Expired"
 ahost="somerandomhostname.whocares.local"
 agtOctet1=random.randint(1,254)
 agtOctet2=random.randint(1,254)
 agtOctet3=random.randint(1,254)
 agtOctet4=random.randint(1,254)
 agt=str(agtOctet1) + "." + str(agtOctet2) + "." + str(agtOctet3) + "." + str(agtOctet4) 
 av="7.0.7.7286.0" 
 at="superagent_ng"
 dvcOctet1=random.randint(1,254)
 dvcOctet2=random.randint(1,254)
 dvcOctet3=random.randint(1,254)
 dvcOctet4=random.randint(1,254)
 dvc=str(dvcOctet1) + "." + str(dvcOctet2) + "." + str(dvcOctet3) + "." + str(dvcOctet4)
 eventAnnotationStageUpdateTime=random.randint(1451606400000,1462060800000) 
 eventAnnotationModificationTime=random.randint(1451606400000,1462060800000)
 eventAnnotationAuditTrail="1," + str(random.randint(1451606400000,1462060800000)) + ",root,Queued" 
 eventAnnotationVersion=1 
 eventAnnotationFlags=0 
 eventAnnotationEndTime=random.randint(1451606400000,1462060800000)
 eventAnnotationManagerReceiptTime=random.randint(1451606400000,1462060800000) 
 _cefVer="0.1"
 message= str(eventSeparator) + "severity=" + str(severity) + " relevance=" + str(relevance) + " assectCriticality=" + str(assetCriticality) + " priority=" + str(priority) + " art=" + str(art) + " cat=" + str(cat) + " deviceSeverity=" + str(deviceSeverity) + " act=" + str(act) + " src=" + str(src) + " spt=" + str(spt) + " dst=" + str(dst) + " dpt=" + str(dpt) + " destinationServiceName=" + str(destinationServiceName) + " destinationGeoCountryCode=" + str(destinationGeoCountryCode) + " destinationGeoLocationInfo=" + str(destinationGeoLocationInfo) + " dlong=" + str(dlong) + " dlat=" + str(dlat) + " destinationGeoPostalCode=" + str(destinationGeoPostalCode) + " destinationGeoRegionCode=" + str(destinationGeoRegionCode) + " cs1=" + str(cs1) + " cs2=" + str(cs2) + " cs3=" + str(cs3) + " cs4=" + str(cs4) + " cs6=" + str(cs6) + " cn1=" + str(cn1) + " locality=" + str(locality) + " cs1Label=" + str(cs1Label) + " cs2Label=" + str(cs2Label) + " cs3Label=" + str(cs3Label) + " cs4Label=" + str(cs4Label) + " cs5Label=" + str(cs5Label) + " cs6Label=" + str(cs6Label) + " cn1Label=" + str(cn1Label) + " cn2Label=" + str(cn2Label) + " cn3Label=" + str(cn3Label) + " deviceCustomDate1Label=" + str(deviceCustomDate1Label) + " deviceCustomDate2Label=" + str(deviceCustomDate2Label) + " ahost=" + str(ahost) + " agt=" + str(agt) + " av=" + str(av) + " at=" + str(at) + " dvc=" + str(dvc) + " eventAnnotationStageUpdateTime=" + str(eventAnnotationStageUpdateTime) + " eventAnnotationModificationTime=" + str(eventAnnotationModificationTime) + " eventAnnotationAuditTrail=" + str(eventAnnotationAuditTrail) + " eventAnnotationVersion=" + str(eventAnnotationVersion) + " eventAnnotationFlags=" + str(eventAnnotationFlags) + " eventAnnotationEndTime=" + str(eventAnnotationEndTime) + " eventAnnotationManagerReceiptTime=" + str(eventAnnotationManagerReceiptTime) + "_cefVer=0.1" 
 print(message)

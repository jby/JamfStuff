#!/bin/bash

RESULT=NO

if [[ -d /Applications/Confer.app ]]
then
    UNINSTALL="/Applications/Confer.app/uninstall"
fi

if [[ -d "/Applications/VMware Carbon Black Cloud" ]]
then
    UNINSTALL="/Applications/VMware Carbon Black Cloud/uninstall.bundle/Contents/MacOS/uninstall"
fi

BYPASS=$("${UNINSTALL}" --check-bypass)

if [[ ${BYPASS} = "Bypass is enabled" ]]
then
    RESULT=YES
fi

echo "<result>${RESULT}</result>"
#!/bin/bash

# Get a list of all applications
applications=$(kubectl get applications -o json | jq -r '.items[].metadata.name')

# Loop through each application and patch to remove finalizers
for app in $applications; do
    echo "Patching application $app to remove finalizers..."
    kubectl patch application $app -p '{"metadata":{"finalizers":null}}' --type=merge
done



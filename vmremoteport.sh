#!/bin/bash
# reset remote RDP port

read -p "Enter the VM Name: "  vm_name
read -p "Enter Port Number: "  port
VBoxManage modifyvm $vm_name --vrdeport $port

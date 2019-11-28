# Process Info Collector

This repository provides an Ansible role and a python script which can be used to fetch running processes information from Linux systems.

## Motivation

System process information can provide valuable insights on the kind of software/workloads running in a system. While most of this information can easily be gathered with "ps", collecting this information in a standard format from multiple systems is not trivial.

## Prerequisites

Ansible 2.6+ on the controller system
Python3 in the target systems

## Approach

A predefined list of specific information files and paths is retrieved from the /proc filesyst3em


## How to use

Test in a local system:

```bash
sudo scripts/collect.py
```

Run on one or more hosts saving the results in the _output/_ directory.

```bash
mkdir output
TARGET=ansible_target_host_or_group
ansible-playbook playbook/collect.yaml -e target=$TARGET
```

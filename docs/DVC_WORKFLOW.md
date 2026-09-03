# DVC Workflow

## Remote
A local DVC remote was configured using:
~/dvc-remote-storage

## Workflow

For Dataset Version 1:

dvc add
git add
git commit
dvc push

For Dataset Version 2:

dvc add
git add
git commit
dvc push

## Version Comparison

dvc diff was used to compare dataset versions.

## Version Restoration

git checkout was used to restore the historical .dvc pointer.

dvc checkout was then used to restore the actual dataset.

## Dataset Versions

Version 1: 150 rows
Version 2: 170 rows
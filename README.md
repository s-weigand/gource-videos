# Create gource videos on the CI

This is my Repo to create [gource](https://github.com/acaudwell/Gource) videos for some selected projects via github actions with [`workflow_dispatch`](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/).

This repo uses [gource-action](https://github.com/NBprojekt/gource-action), which again uses [gource](https://github.com/acaudwell/Gource), so if you like project make sure to leave them some stars too.

<div align="center">

[![gource demo video](https://img.youtube.com/vi/NjUuAuBcoqs/0.jpg)](https://www.youtube.com/watch?v=NjUuAuBcoqs "gource demo video")

</div>

## How does it work?

The main branch contains a basic workflow to create a video with [gource](https://github.com/acaudwell/Gource), which is mainly for testing and having a base to extend from.
It also contains a folder with avatars for commonly used bots (at least the ones I use, PRs welcome).
Each branch contains repository specific avatars and an adjusted version of the workflow (`git_url`, `gource_title`, etc. [see gource-action for all the options](https://github.com/NBprojekt/gource-action)).

## Making your own videos

1. Fork this repo
1. Add your feature branch (I name mimne like the repo it creates a videos for).
1. Add the avatars needed for your project to `repo-avatars`.
1. Adjust the workflow to that repos needs.
1. Got to the `Actions` panel of your fork, click `Create Gource Video` and `Run workflow`, select the branch you want to make a video for and click the `Run workflow` button at the dropdown.
1. Wait for the video to created and enjoy.

### Retrieving avatars for a project

To get the user avatars for a repository you can use the [pearl script provided by gource](https://github.com/acaudwell/Gource/wiki/Gravatar-Example) and copy the files over to the folder `repo-avatars`.

Or you can use the python package [gitfaces](https://github.com/nschloe/gitfaces) as follows from the root of your fork.

```console
$ gitfaces <local-git-repo-path> repo-avatars/
```

Note that it is not always possible to get all avatars, so you might need to do some manual fixing. Gource associates the avatars by their usernames and the images should follow the pattern `<username>.<file_extension>`.
To test locally that you have all avatars, just run `prepare-build.py` and gource as follows

```console
$ python prepare-build.py
$ gource <local-git-repo-path> --user-image-dir avatars/
```

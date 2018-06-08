# Code Climate Bandit engine

This is a [Code Climate](https://codeclimate.com/) engine for running [Bandit](https://wiki.openstack.org/wiki/Security/Projects/Bandit), which "is a security linter for Python source code".

## Build bandit docker image

```
docker build -t codeclimate/codeclimate-bandit .
```

## Command to run code climate locally

```
docker run \
--interactive --tty --rm \
--env CODECLIMATE_CODE="<code_directory>" \
--volume <code_directory>:/code \
--volume /var/run/docker.sock:/var/run/docker.sock \
--volume /tmp/cc:/tmp/cc \
codeclimate/codeclimate analyze -e bandit --dev
```

## See also

* [Building a Code Climate Engine](https://docs.codeclimate.com/docs/building-a-code-climate-engine)
* [Question to Bandit team about building an engine](https://answers.launchpad.net/bandit/+question/280927)

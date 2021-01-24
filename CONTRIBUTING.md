# Contributing to Alexa-skills-starters
Try adding new skills to test on Alexa. Contributing to this project is as easy and transparent as possible, whether it's:

- Reporting a bug
- Submitting a new skill
- Improvising existing skills

## We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.

## Working on the skill and extracting the contents:

- Visit https://developer.amazon.com/alexa/console/ask/create-new-skill to create a new skill.
- After completing the skill, select the skill from the list of skills.
- Click on the Code Tab.
- On the top-left corner, click Download Skill.
- After downloading, extract the contents.
- On extracting the contents, there will be a folder with the following files:
    -interactionModels
    -lambda
    -skill.json

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork this repository and clone to your local system.
2. Go to the location where it is cloned and add a folder named 'ALEXA_SKILL_NAME'.
3. Add only the interactionModels and lambda files from the extracted contents, along with an additional file(.txt or .md) to describe the skill.
4. Commit and push the changes to the forked repository.
5. Make sure to send the pull request to develop branch.

## Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issues](https://github.com/briandk/transcriptase-atom/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](); it's that easy!

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports. I'm not even kidding.

## Use a Consistent Coding Style
I'm again borrowing these from [Facebook's Guidelines](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md)

* 2 spaces for indentation rather than tabs
* You can try running `npm run lint` for style unification

## License
By contributing, you agree that your contributions will be licensed under its MIT License.

## References
This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md)

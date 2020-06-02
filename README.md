# GitLab-BurnDown-Chart-Python

This python script allows you to plot a burndown chart for the estimated hours remaining in your gitlab tasks for the past two weeks. If you run this script on daily basis, it can be used to display your sprint progress.

The python script pulls the estimated hours for all issues with ToDo and InProgress label in your Gitlab group or project.

### Usage

Initialize `GroupID` variable to the ID of the gitlab project or group for which you want to pull issues.

Initialize `GitlabPrivateToken` variable to your gitlab personal access token, available at https://gitlab.com/profile/personal_access_tokens 

If you want to pull issues on some other labels or other criteria, you can make changes to `cmd1` and `cmd2`. It is highly recommended to consult Gitlab Issues API for this purpose, available at https://docs.gitlab.com/ee/api/issues.html.

The `issues.csv` file is provided as a reference to show sample output of the project. You can always delete it or edit it.

By default, the burndown chart is plotted for previous 2 weeks or 14 days. To make changes to the number of days plotted, you can change the variable `chart_plot_days`.

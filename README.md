# GitLab-BurnDown-Chart-Python

This python script allows you to plot a burndown chart for the estimated hours remaining in your gitlab tasks against the date. If you run this script on daily basis, it can be used to display your sprint progress.

### Usage

Initialize `GroupID` variable to the ID of the gitlab project or group for which you want to pull issues.

Initialize `GitlabPrivateToken` variable to your gitlab personal access token, available at https://gitlab.com/profile/personal_access_tokens 

By default, this python script pulls the estimated hours for all issues with ToDo and InProgress label in a Gitlab group. However, you can pull issues related to any group or project with some or all labels, and any other criteria, by making changes to variables `cmd1` and `cmd2`. For this purpose, it is highly recommended to consult Gitlab Issues API, available at https://docs.gitlab.com/ee/api/issues.html.

The `issues.csv` file is provided as a reference to show sample output of the project. You can always delete it or edit it to suit your requirements.

By default, the burndown chart is plotted for previous 2 weeks or 14 days. To make changes to the number of days plotted, you can change the variable `chart_plot_days`.

# 18217041_API_TST
# Purpose
API Todo dibutuhkan para pengguna untuk mengelola seluruh tugas-tugas yang harus dilakukan. Oleh karena itu, pada API ini terdapat methods yang disediakan kepada pengguna untuk mengelola (CRUD) tugas-tugas yang harus dilakukan sehingga dapat meningkatkan fokus dan produktivitas kerja dengan mengintegrasikan situs maupun aplikasi mereka dengan fitur to-do-list.

# Methods & API’s Base URL
Method	Endpoint	                  Usage
GET	    /api/<user>/tasks/<task_id>	Returns specific to-do-task
GET   	/api/<user>/tasks/	        Return all to-do tasks
POST	  /api/<user >/tasks/       	Creates a new to-do-task 
PUT	    /api/<user>/tasks/<task_id>	Updates specific to-do-task
DELETE	/api/<user>/tasks/<task_id>	Deletes specific to-do-task


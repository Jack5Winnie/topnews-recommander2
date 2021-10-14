heroku login
git init
heroku git:remote -a topnews-recommender2
** set git remote heroku to https://git.heroku.com/topnews-recommender2.git
git add .
git commit -am "12/13 v3.6.10 Rebalance positive/neqative..."
git push heroku master

heroku logs --tail
## Login

- Endpoints:
  - POST: auth/login

## Register

- Endpoints:
  - POST: auth/register

## Home

- Endpoints:
  - GET: user/get-real-name
  - GET: songs/get-all-in-session
  - GET: votes/get-summary-in-session
  - POST: votes/vote-up
  - POST: votes/vote-down
  - POST: songs/upload

## AllSongs component

- Endpoints:
  - GET: songs/get-all
  - POST: songs/upload-direct
  - PUT: songs/rename
  - DELETE: songs/delete

## YetToBeApprovedSongs component

- Endpoints:
  - GET: pending-songs/get-all
  - POST: pending-songs/approve
  - DELETE: pending-songs/disapprove

## VotingSessions component

- Endpoints:
  - GET: voting-sessions/get-all
  - POST: voting-sessions/add
  - PUT: voting-sessions/update
  - DELETE: voting-sessions/delete

## TV Diagram

- Endpoints:
  - /get-summary-of-votes-in-session

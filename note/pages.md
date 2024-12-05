# Pages:

## Login
- A login page.
- Fields:
  - Username
  - Password

## Register
- A registration page.
- Fields:
  - Username
  - Email
  - OM
  - Password

## Home
- A list of votable songs with the following functions:
  - Play
  - Vote
- OR, a title indicating there is no voting session at the moment.
- A diagram showing the current voting status OR a title indicating no voting session is active.
- A button to upload a song:
  - Function: Max 30 seconds of audio.
  - The song is placed in a table containing songs awaiting approval.

## Admin
- A responsive sidebar to navigate between different MainComponents.

### MainComponents:
- **MainComponent 1**: 
  - A list showing all songs with the following functions:
    - Play
    - Rename
    - Delete
    - Upload new song by admin
- **MainComponent 2**: 
  - A list showing uploaded songs awaiting approval with the following functions:
    - Play
    - Approve
    - Disapprove
- **MainComponent 3**: 
  - A list of all voting sessions with the following functions:
    - Add new session
    - Delete session
    - View ended sessions (show duration, song names included in the session, and the winning song)
    - View current/future sessions (change duration, add/remove songs, view votes)

## TV Diagram
- A diagram to show the current status of the voting session.

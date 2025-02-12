To make the endpoints more RESTful, we need to follow REST principles, which include using nouns for resources and HTTP methods to perform actions on those resources. Here is a revised version of the endpoints:

1. **AppController**:
    - `/api/app` (unchanged)

2. **AuthController**:
    - `/api/auth/login` (unchanged)
    - `/api/auth/register` (unchanged)
    - `/api/auth/register-dev` (unchanged)

3. **PendingSongsController**:
    - `/api/pending-songs` (GET for `get-all`, POST for `approve`, DELETE for `disapprove`)
    - `/api/pending-songs/audio` (GET for `get-audio`)

4. **SongsController**:
    - `/api/songs` (GET for `get-all`, PUT for `rename`, DELETE for `delete`)
    - `/api/songs/session` (GET for `get-all-in-session`)
    - `/api/songs/session/audio` (GET for `get-all-audio-in-session`)
    - `/api/songs/winner` (GET for `get-winner`)
    - `/api/songs/winner/audio` (GET for `get-winner-audio`)
    - `/api/songs/audio` (GET for `get-audio`, POST for `upload`)
    - `/api/songs/audio/direct` (POST for `upload-direct`)
    - `/api/songs/server/update` (GET for `update-audio`)
    - `/api/songs/server/start` (GET for `start-audio`)
    - `/api/songs/server/stop` (GET for `stop-audio`)

5. **TvController**:
    - `/api/tv/session` (GET for `get-summary-of-votes-in-session`)

6. **UserController**:
    - `/api/users` (GET for `get-all`, PUT for `update-user-pass`)
    - `/api/users/roles` (PUT for `update-user-role`)
    - `/api/users/real-name` (GET for `get-real-name`)

7. **VotesController**:
    - `/api/votes/session` (GET for `get-summary-in-session`)
    - `/api/votes/current-user` (GET for `get-voted-songs-by-user-id`)
    - `/api/votes` (POST for `vote-up`, DELETE for `vote-down`)

8. **VotingSessionController**:
    - `/api/voting-sessions` (GET for `get-all`, POST for `create`, PUT for `update`, DELETE for `delete`)

9. **ViewController**:
    - `/view/tv` (unchanged)
    - `/view/pending-songs` (unchanged)

Here is an example of how to update the `PendingSongsController`:

```typescript
import { Controller, Get, Post, Delete } from '@nestjs/common';

@Controller('api/pending-songs')
export class PendingSongsController {
  @Get()
  getAll() {
    // logic to get all pending songs
  }

  @Get('audio')
  getAudio() {
    // logic to get audio of pending songs
  }

  @Post()
  approve() {
    // logic to approve a pending song
  }

  @Delete()
  disapprove() {
    // logic to disapprove a pending song
  }
}
```

Apply similar changes to other controllers to make the endpoints more RESTful.
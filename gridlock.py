<!doctype html>
<html>
<head>
  <title>2 Player Board Game</title>
  <style>
    body { font-family: sans-serif; }
    .board { display: grid; grid-template-columns: repeat({{ state.board_size[0] }}, 50px); gap: 2px; }
    .cell { width: 50px; height: 50px; border: 1px solid #ccc; display: flex; align-items: center; justify-content: center; }
    .black { background-color: black; color: white; }
    .yellow { background-color: yellow; color: black; }
    button { width: 100%; height: 100%; border: none; background: transparent; cursor: pointer; font-size: 16px; }
  </style>
</head>
<body>
  <h1>2 Player Board Game</h1>

  {% if state.winner is not none %}
    <h2 style="color: green;">🎉 Winner: {{ state.players[state.winner].name }} 🎉</h2>
  {% endif %}

  <p>Current turn: {{ state.players[state.turn].name }} ({{ state.players[state.turn].color }})</p>
  <p>Scores: Player 1 - {{ state.scores[0] }}, Player 2 - {{ state.scores[1] }}</p>

  <div class="board">
    {% for y in range(state.board_size[1]) %}
      {% for x in range(state.board_size[0]) %}
        {% set piece = None %}
        {% for p in state.pieces %}
          {% if p.x == x and p.y == y %}
            {% set piece = p %}
          {% endif %}
        {% endfor %}
        <div class="cell {% if piece %}{{ state.players[piece.player_id].color }}{% endif %}">
          {% if not piece and not state.winner %}
            <form method="POST" action="{{ url_for('move') }}">
              <input type="hidden" name="x" value="{{ x }}">
              <input type="hidden" name="y" value="{{ y }}">
              <button type="submit">.</button>
            </form>
          {% elif piece %}
            {{ state.players[piece.player_id].name[-1] }}
          {% endif %}
        </div>
      {% endfor %}
    {% endfor %}
  </div>

  <p>
    <a href="{{ url_for('reset') }}">Reset Game</a> |
    <a href="{{ url_for('load') }}">Load Saved Game</a>
  </p>
</body>
</html>

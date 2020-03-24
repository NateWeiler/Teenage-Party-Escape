INSERT INTO users
  (username, password)
VALUES
  ('Mom', 'momma'),
  ('Dad', 'pops'),
  ('friend', 'bf'),
  ('you', 'escape')

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2020-01-01 00:00:00');
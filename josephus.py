def kill(people, start_index, delta):
  live_count = len(people)
  current_index = start_index % len(people)

  while live_count > 1:
      skipped = 0
      while skipped <= delta:
          current_index += 1
          if current_index == len(people): current_index = 0
          if people[current_index]: skipped += 1

      people[current_index] = False
      live_count -= 1

  for person in people:
      if person: return person
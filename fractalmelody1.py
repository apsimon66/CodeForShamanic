import mido

# convert midi note number to pitch
def get_note_name(n):
  ps=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
  o=(n//12)-2
  p=ps[n%12]
  return F"{p}{o}"

#print pattern as note names
def print_pattern(pattern):
  notes=[]
  for n in pattern:
    notes.append(get_note_name(n))
  s=","
  s=s.join(notes)
  print(s)
 
#branch the seed pitch two semitones either direction 
def produce_branch(seed):
  return [seed+2,seed-2]
  
def grow_tree(seedlist, iterations, countervar):
  if countervar >= iterations:
    return seedlist
  else:
    pattern0=[]
    pattern0.extend(seedlist)
    pattern1=[]
    for n in pattern0:
      pattern1.extend(produce_branch(n))
    pattern0.extend(pattern1)
    countervar=countervar+1
    pattern0.extend(grow_tree(pattern1,iterations,countervar))
    return pattern0

if __name__ == '__main__':
  seedpitch=[64]
  count=0
  pitches=grow_tree(seedpitch,8,count)
  song=mido.MidiFile()
  track=mido.MidiTrack()
  song.tracks.append(track)

  for n in pitches:
    track.append(mido.Message('note_on',note=n,velocity=64,time=0))
    track.append(mido.Message('note_off',note=n,velocity=127,time=120))
    
  song.save('fractal6.mid')
  print('done')  
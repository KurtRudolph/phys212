task default: [:update]

task :update do
  `git add .`
  `git commit -m "update"`
  `git push`
end

task :prelecture do
   prelecture_number = STDIN.gets.chomp
   entry_name = "PreLectures/prelecture_#{prelecture_number}.md"
  `touch #{entry_name}`
  `echo "# $(date)" >> #{entry_name}`
  system "vim #{entry_name}"
end

task :quicknote do
   entry_name = "QuickNotes/quick_note_#{Time.now.to_s.gsub(/[-\ :]+/, '.').gsub(/.0500+/,'')}.md"
  `touch #{entry_name}`
  `echo "# $(date)" >> #{entry_name}`
  system "vim #{entry_name}"
  `git add #{entry_name}`
  `git commit -m "updates"`
  `git push`
end

task :lecture do
  lecture_number = STDIN.gets.chomp
  entry_name = "Lectures/lecture_#{lecture_number}.md"
  puts entry_name
  `touch #{entry_name}`
  `echo "# $(date)" >> #{entry_name}`
  system "vim #{entry_name}"
end

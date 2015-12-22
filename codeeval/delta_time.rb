require 'time'
File.open(ARGV[0]).each_line do |line|
   time1, time2 = line.split.map(&Time.method(:parse))
   puts (Time.new(0) + (time1 - time2).abs).strftime('%H:%M:%S')
end

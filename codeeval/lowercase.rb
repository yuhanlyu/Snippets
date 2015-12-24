File.open(ARGV[0]).each_line.map(&:downcase).map(&method(:puts))

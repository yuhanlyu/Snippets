puts File.open(ARGV[0]).each_line.map(&:to_i).inject(:+)

File.open(ARGV[0]).each_line.map {|x| puts x.to_i.even? ? 1 : 0 }

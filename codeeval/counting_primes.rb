require 'prime'
File.open(ARGV[0]).each_line do |line|
    n, m = line.split(",").map(&:to_i)
    puts Prime.each(m).count {|p| p >= n}
end

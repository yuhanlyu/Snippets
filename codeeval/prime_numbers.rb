require 'prime'
File.open(ARGV[0]).each_line do |line|
    puts Prime.each(line.to_i - 1).map(&:to_s).join(",")
end

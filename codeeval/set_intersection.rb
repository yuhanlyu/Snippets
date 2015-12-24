require 'set'
File.open(ARGV[0]).each_line do |line|
    puts line.split(";").map { |s| s.split(",").map(&:to_i).to_set }
                        .inject(:&).to_a.join(",")
end

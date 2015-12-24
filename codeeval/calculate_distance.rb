require "scanf"
File.open(ARGV[0]).each_line do |line|
    line.scanf("(%d,%d) (%d,%d)") {|x1, y1, x2, y2|
        puts Math.hypot((x1 - x2).abs, (y1 - y2).abs).round}
end

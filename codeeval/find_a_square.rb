require 'scanf'
File.open(ARGV[0]).each_line do |line|
    ps = line.split(", ").map {|l| l.scanf("(%d,%d)") } 
    if ps.uniq.size < 4
        puts "false"
    else
        x, y = ps.inject([0, 0]) {|(cx, cy),(ax, ay)| 
                [cx + ax, cy + ay]}.map {|x| x.quo(4)}
        v, v2 = [ps[0][0] - x, ps[0][1] - y], [-(ps[0][1] - y), ps[0][0] - x]
        puts (ps.include?([x - v[0], y - v[1]]) &&
              ps.include?([x + v2[0], y + v2[1]]) &&
              ps.include?([x - v2[0], y - v2[1]])).to_s
    end
end

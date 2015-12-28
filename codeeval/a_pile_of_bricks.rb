require 'scanf'
File.open(ARGV[0]).each_line do |line|
    hole, bricks = line.split("|")
    hx, hy = hole.scanf("[%d,%d] [%d,%d]") {|a,b,c,d| [(a-c).abs, (b-d).abs]}[0]
    fit = lambda {|bx, by| (bx <= hx && by <= hy) || (by <= hx && bx <= hy)}
    ans = bricks.split(";").each_with_object([]) {|brick, ans|
        brick.scanf("(%d [%d,%d,%d] [%d,%d,%d])") {|id,x1,y1,z1,x2,y2,z2|
            x, y, z = [(x1 - x2).abs, (y1 - y2).abs, (z1 - z2).abs]
            ans << id if fit.(x, y) or fit.(y, z) or fit.(x, z)
        }
    }
    puts ans.empty? ? "-" : ans.sort.join(",")
end

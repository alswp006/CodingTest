select count(*) FISH_COUNT
from fish_info i, (select fish_type from fish_name_info
                   where fish_name = "BASS" or fish_name = "SNAPPER") n
where i.fish_type = n.fish_type 
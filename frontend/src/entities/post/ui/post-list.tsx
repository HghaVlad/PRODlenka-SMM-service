import { ScrollArea } from "@/shared/ui/scroll-area";
import { FC } from "react";
import { usePostStore } from "..";
import { cn } from "@/shared/lib";

export type Channel = {
  id: number,
  name: string,
  chat_id: number,
  is_group: boolean,
}

export const PostList: FC<{ items: Channel[] }> = ({ items }) => {
  const { selectedPost, setSelectedPost } = usePostStore();
  return (
    <ScrollArea className="h-full w-full">
      <div className="flex flex-col gap-2 pt-0 pr-2">
        {items.map((item) => (
          <button
            key={item.id}
            className={cn(
              "flex flex-col items-start gap-2 rounded-lg border p-3 text-left text-sm transition-all w-full hover:bg-accent",
              selectedPost?.id === item.id && "bg-muted"
            )}
            onClick={() =>
              setSelectedPost(item)
            }
          >
            <div className="flex w-full flex-col gap-1">
              <div className="flex items-center">
                <div className="flex items-center gap-2">
                  <div className="font-semibold">{item.name}</div>
                </div>
              </div>
            </div>
            <div className="line-clamp-2 text-xs text-muted-foreground">
              ID: {item.id}; ChatId: {item.chat_id}
            </div>
          </button>
        ))}
      </div>
    </ScrollArea>
  );
};

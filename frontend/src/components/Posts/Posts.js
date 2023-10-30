import React from "react";
import { FlatList, View } from "react-native";
import Post from "../Post/Post";
import styles from "./styles";

function Posts({ data }) {
  return (
    <View>
      <FlatList
        data={data}
        renderItem={({ item }) => {
          return <Post item={item} />;
        }}
        keyExtractor={(item) => `${item.id_}`}
      />
    </View>
  );
}

export default Posts;

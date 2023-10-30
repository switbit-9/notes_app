import React from "react";
import { StyleSheet, View } from "react-native";
import AnimatedLoader from "react-native-animated-loader";
import styles from "./styles";

function AppLoader() {
  return (
    <View style={[StyleSheet.absoluteFillObject, styles.container]}>
      <AnimatedLoader
        source={require("../../assets/load.json")}
        overlayColor="rgba(255,255,255,0.75)"
        loop
        visible={true}
      />
    </View>
  );
}

export default AppLoader;

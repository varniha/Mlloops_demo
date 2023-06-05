import React from "react";
import { SidebarMenu } from "../../components/SidebarMenu/SidebarMenu";
import { WebhookPage } from "../WebhookPage/WebhookPage";
import { DangerZone } from "./DangerZone";
import { GeneralSettings } from "./GeneralSettings";
import { InstructionsSettings } from "./InstructionsSettings";
import { LabelingSettings } from "./LabelingSettings";
import { MLmonitorsettings } from "./MLmonitorsettings";
import { MachineLearningSettings } from "./MachineLearningSettings/MachineLearningSettings";
import { StorageSettings } from "./StorageSettings/StorageSettings";
import { MLmodifier } from "./ML_Modifier";

export const MenuLayout = ({ children, ...routeProps }) => {
  return (
    <SidebarMenu
      menuItems={[
        GeneralSettings,
        LabelingSettings,
        InstructionsSettings,
        MLmodifier,
        MachineLearningSettings,
        MLmonitorsettings,
        StorageSettings,
        WebhookPage,
        DangerZone,
      ]}
      path={routeProps.match.url}
      children={children}
    />
  );
};

export const SettingsPage = {
  title: "Settings",
  path: "/settings",
  exact: true,
  layout: MenuLayout,
  component: GeneralSettings,
  pages: {
    InstructionsSettings,
    LabelingSettings,
    MLmodifier,
    MachineLearningSettings,
    MLmonitorsettings,
    StorageSettings,
    WebhookPage,
    DangerZone,
    
  },
};
